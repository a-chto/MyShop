const currentImage = document.querySelector('.gallery__current img');
const galleryPreviews = document.querySelector('.gallery__preview');

if (galleryPreviews) {
    galleryPreviews.forEach(function(element) {
        element.addEventListener('click', function(event) {
            const image = element.querySelector('.gallery__image');
            if (!element.classList.contains('gallery__preview_active')) {
                currentImage.src = image.src;
                galleryPreviews.forEach(function(item) {
                    item.classlist.remove('gallery__preview_active')
                })
                element.classList.add('gallery__preview_active');
            }
        })
    })
}