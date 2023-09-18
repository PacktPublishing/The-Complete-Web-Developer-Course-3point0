<?php 
    $hash = password_hash("mypassword", PASSWORD_DEFAULT);

    echo $hash;

    echo "<br><br>";

    if(password_verify("mypassword2", $hash)) {
        echo "Password is valid!";
    }
    else {
        echo "Invalid password!";
    }

?>