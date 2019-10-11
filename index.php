<?php
    $hostname = 'remotemysql.com:3306';
    $username = '3sRxPqRiLy';
    $password = 'dhpwyt9ufA';
    $database = '3sRxPqRiLy';
	
	$db = mysqli_connect($hostname,$username,$password,$database);
	
?>

<html>

	<head>
		<title>Test1</title>
	</head>
	
	<body>
		<h1>My First Heading</h1>
		<?php echo "<h1>Failed to submit data</h1>"; ?>
		<p>My first paragraph.</p>
		
	<?php
		$query = "SELECT * FROM test1";
		mysqli_query($db, $query) or die('Error querying database.');

		$result = mysqli_query($db, $query);
		$row = mysqli_fetch_array($result);

		while ($row = mysqli_fetch_array($result)) {
			echo    "
					<tr>
						<td>".$row['asd']."</td>
					</tr>
				";

		}
	?>
	<?php 
		echo "hi"
	?>
	</body>
	
</html>