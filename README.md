Actuellement, l’interface permet d’échanger des messages chiffrés entre plusieurs clients liés à un serveur.

La structure est en étoile, comme le schéma ci-dessous :


client 1 --------- serveur --------- client 2

                      |
                      |
                   client 3

Améliorations à apporter :
- L’authentification à deux facteurs est actuellement réalisée en vérifiant directement l’interface du serveur. Il faudrait plutôt que le code à 6 chiffres soit envoyé par mail.
- Il faut ajouter l’email des clients à la base de données.
- Actuellement, seuls les clients déjà enregistrés dans la base de données peuvent se connecter. Il faudrait ajouter la possibilité pour de nouveaux utilisateurs de créer un compte.
- La communication se fait actuellement avec un chiffrement asymétrique utilisant l’algorithme RSA. On pourrait utiliser les courbes elliptiques, ou opter pour un chiffrement hybride (échange de clés publiques avec un chiffrement asymétrique, puis utilisation d’un chiffrement symétrique une fois les clés échangées).
- Il n’y a pas d’interface graphique, il faudrait en ajouter une.
- Il n’y a actuellement qu’un seul salon de discussion. Il faudrait ajouter la possibilité de créer plusieurs salons.
