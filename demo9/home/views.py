from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"home/index.html",{})

# 2. Página de contacto
def contact(request):
    return render(request, 'home/contact.html')

# 3. Sobre nosotros
def about(request):
    return render(request, 'home/about.html')

# 4. Lista de productos
def products(request):
    return render(request, 'home/products.html')

# 5. Detalles del producto
def product_detail(request, product_id):
    return render(request, 'home/product_detail.html', {'product_id': product_id})

# 6. Blog
def blog(request):
    return render(request, 'home/blog.html')

# 7. Detalle del post del blog
def blog_detail(request, post_id):
    return render(request, 'home/blog_detail.html', {'post_id': post_id})

# 8. Registro de usuario
def register(request):
    return render(request, 'home/register.html')

# 9. Iniciar sesión
def login(request):
    return render(request, 'home/login.html')

# 10. Perfil de usuario
def profile(request):
    return render(request, 'home/profile.html')