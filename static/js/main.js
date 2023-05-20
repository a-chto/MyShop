// слайдер изображений товара
async function postData (urls = '', data={})(
    const response = await fetch(url, {
        method: 'POST',
        credentials : 'same-origin',
        headers : {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    return await response.json();
)
const currentImage = document.querySelector('.gallery__item_current img');
const galleryItems = document.querySelectorAll('.gallery__preview');

galleryItems.forEach(function(element) {
    element.addEventListener('click', function(event) {
        const img = element.querySelector('img');
        if (!element.classList.contains('gallery__preview_active')) {
            currentImage.src = img.src;
            galleryItems.forEach(function(e) {
                e.classList.remove('gallery__preview_active');
            })
            element.classList.add('gallery__preview_active');
        }
    })
})