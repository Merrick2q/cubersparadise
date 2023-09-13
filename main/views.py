from django.shortcuts import render

def product_list(request):
    sample_items = [
        {
            'name': 'Mscube MS3X',
            'quantity': 5,
            'description': 'Puzzle rubik flagship oleh Mscube. Pendiri Mscube adalah mantan designer dari perusahaan pembuat rubik paling terkenal di dunia yaitu Gancube.',
            'image': 'https://www.thecubicle.com/cdn/shop/products/DianSheng-MS3X-3x3-black-internal_1200x1200.jpg?v=1670870380',  
        },
        {
            'name': 'Dayan Tengyun V3 M',
            'quantity': 3,
            'description': 'Rubik Tengyun generasi ketiga dari Dayan yang terkenal dengan putarannya yang sunyi.',
            'image': 'https://www.thecubicle.com/cdn/shop/products/dayan-tengyun-v3-m_1200x1200.jpg?v=1670433801',  
        },
        {
            'name': 'Huameng YS3M',
            'quantity': 7,
            'description': 'Rubik dari perusahaan baru bernama Huameng yang merupakan anak perusahaan perusahaan pembuat rubik terkenal MoYu.',
            'image': 'https://www.thecubicle.com/cdn/shop/products/moyu-huameng-ys3m-standard_grande.jpg?v=1687294228', 
        },
    ]

    return render(request, 'product_list.html', {'items': sample_items})
