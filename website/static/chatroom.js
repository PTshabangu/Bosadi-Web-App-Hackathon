function sendMessage() {
    // Retrieve the message from the input field
    var messageInput = document.getElementById('messageInput');
    var message = messageInput.value;

    // Display the message in the chatroom
    var messagesContainer = document.getElementById('messages');
    messagesContainer.innerHTML += '<div class="message">' + message + '</div>';

    // Clear the input field
    messageInput.value = '';
}
