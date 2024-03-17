 const socket = new WebSocket('ws://localhost:8000/ws/notifications/');

        socket.onmessage = function(event) {
            const data = JSON.parse(event.data);
            if (data.type === 'notification') {
                const notification = data.notification;
                const notificationElement = document.createElement('li');
                notificationElement.textContent = `${notification.title}: ${notification.description}`;
                document.getElementById('notification-list').appendChild(notificationElement);
            }
        };