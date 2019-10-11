<?php
    $hostname = 'remotemysql.com:3306';
    $username = '3sRxPqRiLy';
    $password = 'dhpwyt9ufA';
    $database = '3sRxPqRiLy';
	
	$db = mysqli_connect($hostname,$username,$password,$database);
	
	 if(! $db ) {
		die('Could not connect: ' . mysqli_error());
	 }
	 echo 'Connected successfully';
	 
	
?>

<html>

	<head>
		<title>Test1</title>
	</head>
	
	<body>
		<h1>My First Heading</h1>
		<p>My first paragraph.</p>
		
	<?php
		$query = "SELECT * FROM test2";
		mysqli_query($db, $query) or die('Error querying database.');

		$result = mysqli_query($db, $query);
		
		while ($row = mysqli_fetch_array($result)) {
			echo  "NAME: ".$row['Name']. "    Age: " . $row['Age'];
		}
	?>
	</body>
	
</html>