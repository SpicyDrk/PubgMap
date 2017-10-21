<?php  
$userFolder = $_POST['folderName'];
if (!(file_exists ($userFolder))){
    mkdir($userFolder); 
    $newfolder = $userFolder;
    mkdir($newfolder, 0777);    
} else {
    echo "Team Already Exists!";
}
//mkdir($userFolder); 
//$newfolder = $userFolder;
//mkdir($newfolder, 0777); 
// check to see if it has been created or not using is_dir 
?>