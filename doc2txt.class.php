<?php
class Doc2Txt {
private $filename;

public function __construct($filePath) {
    $this->filename = $filePath;
}

private function read_doc() {
    $fileHandle = fopen($this->filename, "r");
    $line = @fread($fileHandle, filesize($this->filename));   
    $lines = explode(chr(0x0D),$line);
    $outtext = "";
    foreach($lines as $thisline)
      {
        $pos = strpos($thisline, chr(0x00));
        if (($pos !== FALSE)||(strlen($thisline)==0))
          {
          } else {
            $outtext .= $thisline." ";
          }
      }
     $outtext = preg_replace("/[^a-zA-Z0-9\s\,\.\-\n\r\t@\/\_\(\)]/","",$outtext);
    return $outtext;
}

private function read_docx(){

    $striped_content = '';
    $content = '';

    $zip = zip_open($this->filename);

    if (!$zip || is_numeric($zip)) return false;

    while ($zip_entry = zip_read($zip)) {

        if (zip_entry_open($zip, $zip_entry) == FALSE) continue;

        if (zip_entry_name($zip_entry) != "word/document.xml") continue;

        $content .= zip_entry_read($zip_entry, 
zip_entry_filesize($zip_entry));

        zip_entry_close($zip_entry);
    }// end while

    zip_close($zip);

    $content = str_replace('</w:r></w:p></w:tc><w:tc>', " ", $content);
    $content = str_replace('</w:r></w:p>', "\r\n", $content);
    $striped_content = strip_tags($content);

    return $striped_content;
}

public function convertToText() {

    if(isset($this->filename) && !file_exists($this->filename)) {
        return "File Not exists";
    }

    $fileArray = pathinfo($this->filename);
    $file_ext  = $fileArray['extension'];
    if($file_ext == "doc" || $file_ext == "docx" || $file_ext == "DOC" )
    {
        if(($file_ext == "doc") or ($file_ext == "DOC")) {
            return $this->read_doc();
        } else {
            return $this->read_docx();
        }
    } else {
        return "Invalid File Type";
    }
 }
}
?>