<?php
    $stringData = $_POST["data"];

    $fileLocation= json_decode($stringData);

    $folderName=$fileLocation[0]->folderName;

    $myFile = $folderName."pin.json";
    $fh = fopen($myFile, 'w') or die("can't open file");

    fwrite($fh, $stringData);
    fclose($fh);
?>