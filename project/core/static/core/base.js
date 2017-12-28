function openDialog() {
    dialog = document.getElementsByClassName("dialog");
    dialog.className = dialog.className + "dialog-opened";
}

function closeDialog() {
    dialog = document.getElementsByClassName("dialog-opened");
    dialog.className = dialog.className + "dialog";
}

editLinks = document.getElementsByClassName("edit");

for (i = 0; i < editLinks.length; i++) {
    link = editLinks[i];
    link.onclick = function () {
        openDialog();
    }
}
