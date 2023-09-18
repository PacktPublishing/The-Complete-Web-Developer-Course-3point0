<?php
    $link = mysqli_connect("shareddb-q.hosting.stackcp.net", 
                           "users_db-3131371973", 
                           "snuggles123", "users_db-3131371973");

    if(mysqli_connect_error()) {
        die("There was an error connecting to the database.");
    }

    //$queryInsert = "INSERT INTO users (email, password) VALUES ('anotherperson@somewebsite.co.uk', 'sniffles54321')";
    // mysqli_query($link, $queryInsert);

    //$queryUpdate = "UPDATE users SET email = 'someone123@somewebsite.co.uk' WHERE id = '2' LIMIT 1";
    $queryUpdate = "UPDATE users SET password = 'bubbles1776' WHERE email = 'codestarsjpbaugh@gmail.com' LIMIT 1";

    mysqli_query($link, $queryUpdate);

    $query = "SELECT * FROM users";

    if($result = mysqli_query($link, $query)) {
        $row = mysqli_fetch_array($result);

        echo "Your email is " . $row[1] . " and your password is " . $row[2];
    }
   
?>