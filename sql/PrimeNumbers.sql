DECLARE @counter INT = 2;
DECLARE @result VARCHAR(MAX) = '';
DECLARE @innerCounter INT;
DECLARE @isPrime BIT = 1;
WHILE @counter <= 1000 BEGIN
SET @isPrime = 1;
SET @innerCounter = 2;
IF @counter > 1 BEGIN WHILE @innerCounter <= SQRT(@counter) BEGIN IF @counter % @innerCounter = 0 BEGIN
SET @isPrime = 0;
BREAK;
END
SET @innerCounter = @innerCounter + 1;
END
END IF @isPrime = 1 BEGIN
SET @result = @result + CAST(@counter AS VARCHAR(100)) + "&";
END
SET @counter = @counter + 1;
END IF LEN(@result) > 0
SET @result = LEFT(@result, LEN(@result) - 1);
PRINT @result;