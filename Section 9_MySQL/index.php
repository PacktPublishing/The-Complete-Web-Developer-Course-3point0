<?php
    mysqli_connect("shareddb-q.hosting.stackcp.net", "users_db-3131371973", "snuggles123");

    if(!mysqli_connect_error()) {
        echo "Database connection successful!";
    }
    else {
        echo "There was an error connecting to the database!";
    }

?>