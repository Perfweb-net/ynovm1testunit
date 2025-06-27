import { EmailGenerator } from '../src/EmailGenerator';

describe('EmailGenerator', () => {
  it('should generate a correct confirmation email for an event registration', () => {
    const registrationData = {
      userName: 'Jean Dupont',
      userEmail: 'jean.dupont@example.com',
      eventName: 'Conférence Ynov sur le TDD',
      eventDate: new Date('2024-10-26T10:00:00'),
    };

    const emailContent = EmailGenerator.generateConfirmationEmail(registrationData);

    expect(emailContent).toMatchSnapshot();
  });
}); 