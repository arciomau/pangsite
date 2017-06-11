<?php
/*Скрыпт для праверкі беларускіх панграм, v0.1.2
Аўтар - Аляксей Арцёмаў, 2015 */
mb_internal_encoding('UTF-8');
$litary = array('а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж',
                'з', 'і', 'й', 'к', 'л', 'м', 'н', 'о',
                'п', 'р', 'с', 'т', 'у', 'ў', 'ф', 'х',
                'ц', 'ч', 'ш', 'ы', 'ь', 'э', 'ю', 'я');
$delthis=  array('/[[:punct:]^\s]/u','/\d/'); //выдаліць прагалы, пунктуацыю, лічбы
echo "Ваш радок:\n";
$mystr=mb_strtolower(fgets(STDIN));
$mystr1=preg_replace($delthis, null, $mystr); //выдаляем прагалы і канвертуем вялікія літары ў маленькія
echo "Даўжыня сказа - ", mb_strlen($mystr1), " літ.\n";
$arr1=array_unique(str_split($mystr1, 2)); //выдаляем дублі і пішам па 2 байты
$getdiff=array_diff($litary,$arr1); //розніца паміж масівамі
if ($getdiff<>null) //калі маем адрозненні
{
    echo "Да панграмы - ", count($getdiff), " літ.: ";
    foreach ($getdiff as $difflitary) echo $difflitary, " ";
    echo "\n";  
}
else echo "Гэта панграма!\n";
?>