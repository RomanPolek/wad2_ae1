mouse_x = 0
mouse_y = 0

interactive_images = null

window.addEventListener("load", () => {
    interactive_images = document.getElementsByClassName("interactive")
    for(var i = 0; i < interactive_images.length; i++) {
        interactive_images[i].onmouseover = function() {
            this.hovering = true
        }.bind(interactive_images[i])
        interactive_images[i].onmouseout = function() {
            this.hovering = false
        }.bind(interactive_images[i])
    }

    window.addEventListener("mousemove", (event)=>{
        mouse_x = event.clientX
        mouse_y = event.clientY
    })
    window.requestAnimationFrame(update)
})

function update() {
    for(var i = 0; i < interactive_images.length; i++) {
        var br = interactive_images[i].getBoundingClientRect()
        var cx = (br.left + br.right) / 2
        var cy = (br.top + br.bottom) / 2
        var x = mouse_x - cx
        var y = mouse_y - cy
        if(interactive_images[i].hovering) {
            interactive_images[i].style.transition = "none"
            var target = x/13
            var current = 0
            try {
                current = parseFloat(interactive_images[i].style.transform.substring(8, interactive_images[i].style.transform.length-4))
            }
            catch {
            }
            if(isNaN(current)) {
                current = 0
            }
            interactive_images[i].style.transform = `rotateY(${(current + (target - current)/10)}deg)`
        }
        else {
            interactive_images[i].style.transition = "all 1s"
            interactive_images[i].style.transform = "none"
        }
    }
    window.requestAnimationFrame(update)
}