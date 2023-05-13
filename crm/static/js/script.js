const links = document.querySelectorAll('a[class="nav-link"]')

links.forEach(link => {
    link.addEventListener('click', 
    function () {
        links.forEach(link => {
            link.classList.remove('active')
        })
        this.classList.add('active')
        
    })
})

function clearContent() {
    document.body.addEventListener('htmx:beforeRequest', function(event) {
        event.detail.target.innerHTML = ''
    });
}