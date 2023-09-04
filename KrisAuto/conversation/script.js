function scrollToBottom() {
    var messageContainer = document.getElementById('message-container');
    messageContainer.scrollTop = messageContainer.scrollHeight;
}

window.addEventListener('load', scrollToBottom);

var messageForm = document.getElementById('message-form');
messageForm.addEventListener('submit', function() {
    setTimeout(scrollToBottom, 0);
});