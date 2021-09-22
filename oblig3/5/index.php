<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Document</title>
        <link rel="stylesheet" href="../../ForsideStyle.css">
    </head>
    <body>
        <ul>
            <li><a class="active" href="../../index.php">Forside</a></li>
            <li><a class="active" href="../index.php">Tilbake</a></li>
        </ul>
        <?php
        $proveresultater = array(
            array("Sander", "Clausen", "3DAA", 6, "2 timer"),
            array("Linus", "Gylesth", "3DAA", 1, "3 timer"),
            array("Sebastian", "Hauglid", "3DAA", 4, "3 timer"),
            array("Thomas", "Hole", "3DAA", 5, "3 timer"),
            array("Marius", "Jensen", "3DAA", 1, "3 timer")
        );

        echo $proveresultater[0][0].$proveresultater[0][1]." Klasse: ".$proveresultater[0][2]." Karakter: ".$proveresultater[0][3]." tidsforburk: ".$proveresultater[0][4]."<br>";
        echo $proveresultater[1][0].$proveresultater[1][1]." Klasse: ".$proveresultater[1][2]." Karakter: ".$proveresultater[1][3]." tidsforburk: ".$proveresultater[1][4]."<br>";
        echo $proveresultater[2][0].$proveresultater[2][1]." Klasse: ".$proveresultater[2][2]." Karakter: ".$proveresultater[2][3]." tidsforburk: ".$proveresultater[2][4]."<br>";
        echo $proveresultater[3][0].$proveresultater[3][1]." Klasse: ".$proveresultater[3][2]." Karakter: ".$proveresultater[3][3]." tidsforburk: ".$proveresultater[3][4]."<br>";
        echo $proveresultater[4][0].$proveresultater[4][1]." Klasse: ".$proveresultater[4][2]." Karakter: ".$proveresultater[4][3]." tidsforburk: ".$proveresultater[1][4]."<br>";

        ?>
    </body>
</html>