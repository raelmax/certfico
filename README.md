# Certifico

A simple tool to generate certificates to attendees of EventBrite events.

## Server
- Store event information
- Store participant list/csv
- Send a link to print the certificate

## Client
- Generate a certificate preview
- Generate certificate to attendee

## Flow
- Go to certbrite.com and add your certificate header, body and footer;
- Preview your certificate;
- Upload your csv with name and email and click to send certificates;
- Backend fires emails to users from csv with a small text and a link to certificate page;
- User download the certificate pdf from client-side.
- The end.

## TODO
[ ] Email template;
[ ] Form validations;
[ ] Tests
[ ] Created certificate page;
[x] Make mail worker a entry point command;
[x] Refactoring on app configs

- Honcho support
- Theme system;
- Login/Register using social networks;
- See a participants list and resend certificates;
- Layout improvements;
