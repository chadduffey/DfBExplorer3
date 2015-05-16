<?php

$subject = "Moonhunters";
$contactName = $_GET["contactName"];
$contactEmail = urldecode($_GET["contactEmail"]);
$contactMessage = $_GET["contactEmail"];

mail("your@mail.com", $subject, "Message from: $contactName : ".$contactMessage, "From: $contactEmail\n");

echo "Thank you! We will reply soon!";

?>