from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from flask_bcrypt import Bcrypt
from .models import Usuario, Registro
from . import db, login_manager

main = Blueprint('main', __name__)
bcrypt = Bcrypt()

# Cargar usuario en sesión
@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

# Página inicial
@main.route('/')
def inicio():
    return render_template('inicio.html')

# Registro de usuario
@main.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')

        # Verificar si ya existe el email
        usuario_existente = Usuario.query.filter_by(email=email).first()
        if usuario_existente:
            flash("Ese email ya está registrado. Probá con otro.", "danger")
            return redirect(url_for('main.registro'))

        nuevo_usuario = Usuario(nombre=nombre, email=email, password=password)
        db.session.add(nuevo_usuario)
        db.session.commit()
        flash("Usuario creado con éxito. Ya podés iniciar sesión.", "success")
        return redirect(url_for('main.login'))

    return render_template('registro.html')

# Login de usuario
@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        usuario = Usuario.query.filter_by(email=email).first()

        if usuario and bcrypt.check_password_hash(usuario.password, password):
            login_user(usuario)
            flash("Sesión iniciada correctamente.", "success")
            return redirect(url_for('main.dashboard'))
        else:
            flash("Credenciales incorrectas. Revisá tu email y contraseña.", "danger")
            return redirect(url_for('main.login'))

    return render_template('login.html')

# Logout
@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Sesión cerrada correctamente.", "info")
    return redirect(url_for('main.login'))

# Dashboard con ingresos y gastos
@main.route('/dashboard')
@login_required
def dashboard():
    ingresos = Registro.query.filter_by(tipo="Ingreso", usuario_id=current_user.id).all()
    gastos = Registro.query.filter_by(tipo="Gasto", usuario_id=current_user.id).all()

    total_ingresos = sum(r.monto for r in ingresos)
    total_gastos = sum(r.monto for r in gastos)
    saldo = total_ingresos - total_gastos

    return render_template('dashboard.html',
                           ingresos=ingresos,
                           gastos=gastos,
                           total_ingresos=total_ingresos,
                           total_gastos=total_gastos,
                           saldo=saldo)

# Formulario para nuevo registro
@main.route('/nuevo', methods=['GET', 'POST'])
@login_required
def nuevo():
    if request.method == 'POST':
        tipo = request.form['tipo']
        monto = int(request.form['monto'])
        descripcion = request.form['descripcion']

        nuevo_registro = Registro(
            tipo=tipo,
            monto=monto,
            descripcion=descripcion,
            usuario_id=current_user.id
        )
        db.session.add(nuevo_registro)
        db.session.commit()
        flash("Registro agregado correctamente.", "success")
        return redirect(url_for('main.dashboard'))

    return render_template('formulario.html')

# Editar registro existente
@main.route('/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar(id):
    registro = Registro.query.get_or_404(id)

    # Solo permitir editar registros del usuario actual
    if registro.usuario_id != current_user.id:
        flash("No tenés permiso para editar este registro.", "danger")
        return redirect(url_for('main.dashboard'))

    if request.method == 'POST':
        registro.tipo = request.form['tipo']
        registro.monto = int(request.form['monto'])
        registro.descripcion = request.form['descripcion']
        db.session.commit()
        flash("Registro actualizado correctamente.", "success")
        return redirect(url_for('main.dashboard'))

    return render_template('editar.html', registro=registro)

# Eliminar registro existente
@main.route('/eliminar/<int:id>', methods=['POST'])
@login_required
def eliminar(id):
    registro = Registro.query.get_or_404(id)

    # Solo permitir eliminar registros del usuario actual
    if registro.usuario_id != current_user.id:
        flash("No tenés permiso para eliminar este registro.", "danger")
        return redirect(url_for('main.dashboard'))

    db.session.delete(registro)
    db.session.commit()
    flash("Registro eliminado correctamente.", "success")
    return redirect(url_for('main.dashboard'))