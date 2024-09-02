/**
 * Updates the copyright notice on the webpage.
 */
function updateCopyrightNotice() {
    let getYear = new Date().getFullYear()
    let yearID = $('#year')[0]
    if (getYear == 2024) {
        yearID.innerHTML = getYear
    } else {
        yearID.innerHTML = `2024 - ${getYear}`
    }
}

$(document).ready(function () {
    $('.toast').toast('show')

    updateCopyrightNotice()
});

const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]')
const popoverList = [...popoverTriggerList].map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl))