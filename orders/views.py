from django.shortcuts import render

def home(request):
    return render(request, 'restaurant/home.html')
    
    def get_menu(request):
    menu = [
        {
            "name": "Paneer Butter Masala",
            "description": "Creamy tomato curry with soft paneer cubes.",
            "price": 220
        },
        {
            "name": "Veg Biryani",
            "description": "Aromatic basmati rice with vegetables and spices.",
            "price": 180
        },
        {
            "name": "Masala Dosa",
            "description": "Crispy dosa stuffed with spicy potato filling.",
            "price": 90
        },
    ]
    return Response(menu)