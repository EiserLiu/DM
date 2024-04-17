// const socket = new WebSocket('ws://localhost:8000/action/');
//
// socket.onopen = function (event) {
//     console.log('WebSocket connection opened');
// };
//
// socket.onmessage = function (event) {
//     const data = JSON.parse(event.data);
//     const recordsList = data;
//     const recordsElement = document.querySelector('.records');
//     recordsList.forEach(record => {
//         const recordElement = document.createElement('div');
//         recordElement.classList.add('record');
//         recordElement.innerHTML = `
//             <h3>${record.user} -${record.building}</h3>
//             <p>${record.createdat}</p>
//             <p>${record.status}</p>
//         `;
//         recordsElement.appendChild(recordElement);
//     });
// };
//
// socket.onclose = function (event) {
//     console.log('WebSocket connection closed');
// };
//
// socket.onerror = function (error) {
//     console.error('WebSocket error:', error);
// };