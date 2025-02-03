// Clave da API (coloca a túa propia clave da API de Google aquí)
const API_KEY = 'YOUR_API_KEY';

// Calendarios de Google que queres mostrar
const CALENDAR_IDS = [
    '6825cd40528bd6d79a65ccaea061346e75753c02d3a5f44ac8b54747b21cb629@group.calendar.google.com',
    '89713e8c033d4453462a24c4fa17ac13e14eadf4a86693fc00633521c4dee7e0@group.calendar.google.com'
];

// Función para cargar a API de Google
function loadGoogleApi() {
    gapi.load('client', initClient);
}

// Inicializar o cliente da API do Google
function initClient() {
    gapi.client.init({
        'apiKey': "AIzaSyAAykynVd3rr1PgyY7rKitp495x9eqZ6iI",
        'discoveryDocs': ['https://www.googleapis.com/discovery/v1/apis/calendar/v3/rest']
    }).then(function () {
        // Cargar os eventos dos calendarios
        loadCalendarEvents();
    });
}

// Cargar eventos de varios calendarios
function loadCalendarEvents() {
    let allEvents = [];

    // Iterar sobre os calendarios para obter eventos
    CALENDAR_IDS.forEach(calendarId => {
        gapi.client.calendar.events.list({
            'calendarId': calendarId,
            'timeMin': (new Date()).toISOString(),
            'maxResults': 10,
            'singleEvents': true,
            'orderBy': 'startTime'
        }).then(function(response) {
            let events = response.result.items;
            events.forEach(event => {
                allEvents.push({
                    title: event.summary,
                    start: event.start.dateTime || event.start.date,
                    end: event.end.dateTime || event.end.date
                });
            });

            // Renderiza os eventos cando se completan todos
            if (allEvents.length === CALENDAR_IDS.length * 10) {
                renderEvents(allEvents);
            }
        });
    });
}

// Función para renderizar os eventos no calendario
function renderEvents(events) {
    let calendarContainer = $('#calendar');
    calendarContainer.empty(); // Limpa os contidos previos

    if (events.length === 0) {
        calendarContainer.append('<p>No hay eventos para mostrar.</p>');
    } else {
        let eventList = '<ul>';
        events.forEach(event => {
            eventList += `<li><strong>${event.title}</strong> - ${event.start} a ${event.end}</li>`;
        });
        eventList += '</ul>';
        calendarContainer.append(eventList);
    }
}

// Cargar a API cando a páxina estea lista
$(document).ready(function() {
    loadGoogleApi();
});
