const canvas = document.getElementById("my-canvas")
const ctx = canvas.getContext("2d")
canvas.width = window.innerWidth
canvas.height = window.innerHeight

canvas.addEventListener('mousemove', (e) => {
    ctx.beginPath()
    ctx.arc(e.x, e.y, 10, 0, 360)
    ctx.stroke()
})
