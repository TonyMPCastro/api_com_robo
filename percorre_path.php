<?php

$json = file_get_contents("dados_impot_medzin/Pacientes/Split/1_parte_1.json");

$array = json_decode($json,true);

$cont = 0;
foreach ($array as $value) {
    
     echo json_encode($value);
     $cont++;


}

 echo "Quantidade: ".$cont;

?>