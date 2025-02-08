<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Récupérer les données du formulaire
    $name = htmlspecialchars($_POST['name']);
    $email = htmlspecialchars($_POST['email']);
    $message = htmlspecialchars($_POST['message']);

    // Ici, tu pourrais ajouter un code pour envoyer ces informations par email
    // Par exemple, en utilisant la fonction mail() de PHP
    $to = "eriviere@guardiaschool.fr";
    $subject = "Prise de contact";
    $message_content = "Nom: $name\nEmail: $email\nMessage: $message";

    $headers = "From: $email";

    // Envoyer l'email
    if (mail($to, $subject, $message_content, $headers)) {
        echo "Votre message a été envoyé avec succès!";
    } else {
        echo "Désolé, une erreur est survenue. Votre message n'a pas pu être envoyé.";
    }
} else {
    echo "Erreur de méthode.";
}
?>
