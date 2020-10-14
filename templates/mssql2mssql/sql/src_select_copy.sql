SELECT [id]
      ,[recipient_telegram__id]
      ,[telegram_messages_types__id]
      ,[text]
      ,[status_alias]
      ,[error_description]
      ,[created_at]
      ,[created_by]
      ,[created_ip]
      ,[modified_at]
      ,[modified_by]
      ,[modified_ip]
      ,[timestamp]
      ,TODATETIMEOFFSET(convert(datetimeoffset,'<sfDate>',127),'+00:00') as [sfDate]
      ,convert(uniqueidentifier,'<sfUUID>') as [sfUUID]
  FROM [dbo].[telegram_messages]
