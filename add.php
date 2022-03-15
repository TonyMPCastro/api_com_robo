<?php

$data2 = array("admin" => "user_admin",
 "password" => "user_password",
  "user" => "user_user",
 "p1" => "1",
 "wpp" => "telefone"

); 
 
 
$data_string = json_encode($data2);

$ch = curl_init('http://localhost:3000/callback_user_add_smarters');                                                                      
curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");                                                                     
curl_setopt($ch, CURLOPT_POSTFIELDS, $data_string);                                                                  
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);                                                                      
curl_setopt($ch, CURLOPT_HTTPHEADER, array(                                                                          
    'Content-Type: application/json',                                                                                
    'Content-Length: ' . strlen($data_string))                                                                       
);                                                                                                                   

$retorno = curl_exec($ch);

$registros = json_decode($retorno, true);


curl_close($ch);


print_r($registros);
