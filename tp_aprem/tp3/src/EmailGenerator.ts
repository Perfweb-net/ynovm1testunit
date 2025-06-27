interface RegistrationData {
  userName: string;
  userEmail: string;
  eventName: string;
  eventDate: Date;
}

export class EmailGenerator {
  public static generateConfirmationEmail(data: RegistrationData): string {
    const formattedDate = data.eventDate.toLocaleDateString('fr-FR', {
      weekday: 'long', year: 'numeric', month: 'long', day: 'numeric'
    });
    const formattedTime = data.eventDate.toLocaleTimeString('fr-FR', {
      hour: '2-digit', minute: '2-digit'
    });

    return `
Sujet : Confirmation de votre inscription à ${data.eventName}

Bonjour ${data.userName},

Nous avons le plaisir de vous confirmer votre inscription à l'événement : ${data.eventName}.
Celui-ci aura lieu le ${formattedDate} à ${formattedTime}.

Un e-mail de rappel vous sera envoyé 48h avant l'événement.

Cordialement,
L'équipe Ynov
`.trim();
  }
} 