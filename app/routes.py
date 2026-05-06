from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from flask_bcrypt import Bcrypt
from collections import defaultdict
from .models import Usuario, Registro
from . import db, login_manager

main = Blueprint('main', __name__)
bcrypt = Bcrypt()


# ===== LOGIN MANAGER =====
@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))


# ===== HOME =====
@main.route('/')
def inicio():
    return render_template('inicio.html')


# ===== REGISTRO =====
@main.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        password = bcrypt.generate_password_hash(
            request.form['password']
        ).decode('utf-8')

        if Usuario.query.filter_by(email=email).first():
            flash("Ese email ya está registrado.", "danger")
            return redirect(url_for('main.registro'))

        usuario = Usuario(nombre=nombre, email=email, password=password)
        db.session.add(usuario)
        db.session.commit()

        flash("Usuario creado correctamente.", "success")
        return redirect(url_for('main.login'))

    return render_template('registro.html')


# ===== LOGIN =====
@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        usuario = Usuario.query.filter_by(email=email).first()

        if usuario and bcrypt.check_password_hash(usuario.password, password):
            login_user(usuario)
            return redirect(url_for('main.dashboard'))

        flash("Credenciales incorrectas.", "danger")

    return render_template('login.html')


# ===== LOGOUT =====
@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))


# ===== DASHBOARD =====
@main.route('/dashboard')
@login_required
def dashboard():
    ingresos = Registro.query.filter_by(
        tipo="Ingreso",
        usuario_id=current_user.id
    ).order_by(Registro.fecha.desc()).all()

    gastos = Registro.query.filter_by(
        tipo="Gasto",
        usuario_id=current_user.id
    ).order_by(Registro.fecha.desc()).all()

    total_ingresos = sum(r.monto for r in ingresos)
    total_gastos = sum(r.monto for r in gastos)
    saldo = total_ingresos - total_gastos

    # ===== AGRUPAR POR MES (para gráfico línea) =====
    balance_por_mes = defaultdict(float)

    for r in ingresos:
        mes = r.fecha.strftime("%Y-%m")
        balance_por_mes[mes] += r.monto

    for r in gastos:
        mes = r.fecha.strftime("%Y-%m")
        balance_por_mes[mes] -= r.monto

    meses = list(balance_por_mes.keys())
    balances = list(balance_por_mes.values())

    # ===== AGRUPAR POR CATEGORIA (para gráfico pie) =====
    gastos_por_categoria = defaultdict(float)

    for g in gastos:
        categoria = g.categoria if g.categoria else "Otros"
        gastos_por_categoria[categoria] += g.monto

    categorias = list(gastos_por_categoria.keys())
    totales_categorias = list(gastos_por_categoria.values())

    return render_template(
        'dashboard.html',
        ingresos=ingresos,
        gastos=gastos,
        total_ingresos=total_ingresos,
        total_gastos=total_gastos,
        saldo=saldo,
        meses=meses,
        balances=balances,
        categorias=categorias,
        totales_categorias=totales_categorias
    )


# ===== NUEVO REGISTRO =====
@main.route('/nuevo', methods=['GET', 'POST'])
@login_required
def nuevo():
    if request.method == 'POST':
        tipo = request.form['tipo']
        monto = float(request.form['monto'])
        descripcion = request.form['descripcion']
        categoria = request.form['categoria']

        registro = Registro(
            tipo=tipo,
            monto=monto,
            descripcion=descripcion,
            categoria=categoria,
            usuario_id=current_user.id
        )

        db.session.add(registro)
        db.session.commit()

        flash("Registro agregado.", "success")
        return redirect(url_for('main.dashboard'))

    return render_template('formulario.html')


# ===== EDITAR =====
@main.route('/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar(id):
    registro = Registro.query.get_or_404(id)

    if registro.usuario_id != current_user.id:
        return redirect(url_for('main.dashboard'))

    if request.method == 'POST':
        registro.tipo = request.form['tipo']
        registro.monto = float(request.form['monto'])
        registro.descripcion = request.form['descripcion']
        registro.categoria = request.form['categoria']

        db.session.commit()
        return redirect(url_for('main.dashboard'))

    return render_template('editar.html', registro=registro)


# ===== ELIMINAR =====
@main.route('/eliminar/<int:id>', methods=['POST'])
@login_required
def eliminar(id):
    registro = Registro.query.get_or_404(id)

    if registro.usuario_id != current_user.id:
        return redirect(url_for('main.dashboard'))

    db.session.delete(registro)
    db.session.commit()

    return redirect(url_for('main.dashboard'))