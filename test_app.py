from app import app

def test_hello_endpoint():
    cliente = app.test_client()
    respuesta = cliente.get('/hello?name=Estudiante')
    assert respuesta.status_code == 200
    assert b"Hello, Estudiante!" in respuesta.data