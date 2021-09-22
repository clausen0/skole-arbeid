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
           $ArrayGen = array();
           

            for($x = 0; $x < 100; $x++){ 
                $ArrayGen[$x] = rand(0, 1000);
                // echo $ArrayGen[$x]."<br>";
            };
            
            $HighestNumber=$ArrayGen[0];
            $LowestNumber=$ArrayGen[0];
            $counter = 0;

            for($i=0; $i <= count($ArrayGen) -1 ; $i++){
                if ($HighestNumber < $ArrayGen[$i]){
                    $HighestNumber = $ArrayGen[$i];
                }
                if ($LowestNumber > $ArrayGen[$i]){
                    $LowestNumber = $ArrayGen[$i];
                }
                if($ArrayGen[$i] < 499){
                    $counter++;
                }
            }  
            echo $HighestNumber. "<br>";
            echo $LowestNumber. "<br>";
            echo $counter;





        ?>
    </body>
</html>