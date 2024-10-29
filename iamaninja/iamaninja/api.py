from ninja import NinjaAPI, Schema


api = NinjaAPI(urls_namespace='crud')


@api.get('/hello')
def hello(request, name: str | None = None) -> str:
    if name:
        return f'Pozdrawiam wszystich Polaków. I Ciebie {name}, Pielgrzymie'
    return 'Sieg Heil'

@api.get('/math')
def math(request, a: int, b: int) -> dict[str: int]:
    return {'addition': a + b, "subtraction": a - b}

@api.get('/mathalt/{a}and{b}')
def math_alt(request, a: int, b: int) -> dict[str: int]:
    return {'addition': a + b, "subtraction": a - b}


class HelloSchema(Schema):
    name: str = 'dad'


@api.post('/hellopost')
def hello_post(request, data: HelloSchema) -> str:
    return f'Hello Son! Hello: {data.name}'


class UserName(Schema):
    username: str
    is_authenticated: bool
    email: str = None
    first_name: str = None
    last_name: str = None


@api.get('/me', response=UserName)
def me_as_a_person(request):
    return request.user


class UserSchema(Schema):
    username: str
    email: str
    first_name: str
    last_name: str

class Error(Schema):
    message: str

@api.get("/meeh", response={200: UserSchema, 403: Error})
def me(request):
    if not request.user.is_authenticated:
        return 403, {"message": "Please sign in first"}
    return request.user
