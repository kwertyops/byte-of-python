document.addEventListener("DOMContentLoaded", () => {
    let next = document.querySelector(".nav-chapters.next");
    if (next) {
        next.remove();
    }

    let prev = document.querySelector(".nav-chapters.previous");
    if (prev) {
        prev.remove();
    }
});