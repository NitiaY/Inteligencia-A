declare @cadena1 varchar(20),
		@cadena2 varchar(20),
		@longitud_cadena1 int,
		@longitud_cadena2 int,
		@contador int,
		@letra varchar(20),
		@sql nvarchar(4000),
		@columna nvarchar(10)


		set @cadena1='nithya'
		set @cadena2='nitia'
		set @contador=1
		select @longitud_cadena1 = LEN(@cadena1)
		set @sql = 'create table nombre('
		while @contador<=@longitud_cadena1
		begin
			set @letra=LEFT(@cadena1,1)+cast(@contador as varchar(1))+' varchar(2),'
			set @cadena1=RIGHT(@cadena1,LEN(@cadena1)-1)
			set @sql =@sql + @letra
			set @contador=@contador+1
		end
		set @sql = LEFT(@sql, LEN(@sql)-1)
		set @sql = @sql+')'
		print(@sql)

		exec sp_executesql @sql

		--select * from nombre
		--select * from INFORMATION_SCHEMA.COLUMNS
		--where TABLE_NAME = 'nombre'
		--order by ORDINAL_POSITION 


		--set @cadena2 = 'marta'
		set @contador=1
		select @longitud_cadena2 = LEN(@cadena2)
		while(@contador<=@longitud_cadena2)
		begin
			set @letra=LEFT(@cadena2,1)
			set @cadena2=RIGHT(@cadena2,LEN(@cadena2)-1)
			set @columna=(select top 1 COLUMN_NAME
			from INFORMATION_SCHEMA.COLUMNS
			where TABLE_NAME ='nombre'
			and left(COLUMN_NAME,1)=@letra
			and ORDINAL_POSITION>=@contador)

			set @sql= 'insert into nombre('+@columna+') values(1)'

			exec sp_executesql @sql
			set @contador = @contador+1
		end 
		
		select * from nombre
		--drop table nombre
		