<?php

    session_start();
    $error = "";

    //db server: sdb-u.hosting.stackcp.net
    //db name: secretdiary-32313145fa
    //db password: yvcii4u6ve

    if(array_key_exists("logout", $_GET)) {
        session_unset();
        setcookie("id", "", time() - 60 * 60);
        $_COOKIE["id"] = "";
    }
    else if(array_key_exists("id", $_SESSION) OR array_key_exists("id", $_COOKIE)) {
        //go to the loggedinpage if you're still logged in
        header("Location: loggedinpage.php");
    }//end test for logout query string


    if(array_key_exists("submit", $_POST)) {
        
        $link = mysqli_connect("sdb-u.hosting.stackcp.net", 
            "secretdiary-32313145fa", 
            "yvcii4u6ve", 
            "secretdiary-32313145fa");

        if(mysqli_connect_error()) {
            die("Data Connection Error");
        }




        if(!$_POST['email']) {
            $error .= "An email address is required.<br>";
        }

        if(!$_POST['password']) {
            $error .= "A password is required.<br>";
        }

        if($error != "") {
            $error = "<p>There were error(s) in your form!</p>" . $error;
        }
        else {
            $emailAddress = mysqli_real_escape_string($link, $_POST['email']);
            $password = mysqli_real_escape_string($link, $_POST['password']); 
            $password = password_hash($password, PASSWORD_DEFAULT);

            if($_POST['signUp'] == '1') {
                $query  = "SELECT id FROM users WHERE email = '" . $emailAddress . "' LIMIT 1";

                $result = mysqli_query($link, $query);
    
                if(mysqli_num_rows($result) > 0) {
                    $error = "That email address is taken.";
                }
                else {
                    $query = "INSERT INTO users (email, password) VALUES ('" . $emailAddress . "', '" . $password . "')";
    
                    if(!mysqli_query($link, $query)) {
                        $error .= "<p>Could not sign you up - Please try again later.</p>";
                        $error .= "<p>" . mysqli_error($link) . "</p>";
                    }
                    else {
                        $id = mysqli_insert_id($link);
    
                        $_SESSION['id'] = $id;
    
                        if(isset($_POST['stayLoggedIn'])) {
                            setcookie("id", $id, time() + 60 * 60 * 24 * 365);
                        }
    
                        header("Location: loggedinpage.php");
    
                    }//end if for successful/failed sign up
                }//end if mysqli_num_rows test
            }
            else {
                $query = "SELECT * FROM users WHERE email = '" . $emailAddress . "'";
                $result = mysqli_query($link, $query);
                $row = mysqli_fetch_array($result);
                $password = mysqli_real_escape_string($link, $_POST['password']);

                if(isset($row) AND array_key_exists("password", $row)) {
                    $passwordMatches = password_verify($password, $row['password']);

                    if($passwordMatches) {
                        $_SESSION['id'] = $row['id'];
                        if(isset($_POST['stayLoggedIn'])) {
                            setcookie("id", $row['id'], time() + 60 * 60 * 24 * 365);
                        }

                        header("Location: loggedinpage.php");
                    }
                    else {
                        $error = "That email/password combination could not be found.";
                    }//end else - password matches or doesn't
                }
                else {
                    $error = "That email/password combination could not be found.";
                }
            }//end if-else for signUp == 1 or 0
        }//end of error existing check



    }//end if the submit exists

?>

<div id="error"><?php echo $error; ?></div>

<!-- sign up form -->
<form method="post">
    <input type="email" name="email" placeholder="Your email">
    <input type="password" name="password" placeholder="Password">
    <input type="checkbox" name="stayLoggedIn" value="1">
    <input type="hidden" name="signUp" value="1">

    <input type="submit" name="submit" value="Sign Up!">
</form>

<!-- log in form -->
<form method="post">
    <input type="email" name="email" placeholder="Your email">
    <input type="password" name="password" placeholder="Password">
    <input type="checkbox" name="stayLoggedIn" value="1">
    <input type="hidden" name="signUp" value="0">

    <input type="submit" name="submit" value="Log In">
</form>