<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" 
                integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" 
                crossorigin="anonymous"></script>

        <script type="text/javascript">
            $(".toggleForms").click(function() {
                //toggle the forms
                $("#signUpForm").toggle();
                $("#logInForm").toggle();
            });

            $("#diary").bind('input propertychange', function() {
                $.ajax({
                    method: "POST",
                    url: "updatedatabase.php",
                    data: {content: $("#diary").val()}
                });
            });
        </script>
    </body>
</html>