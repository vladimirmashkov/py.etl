IF OBJECT_ID('[ss].[telegram_messages]') IS NOT NULL
BEGIN
  DROP TABLE [ss].[telegram_messages]
END

CREATE TABLE [ss].[telegram_messages](
	[id] [int] NULL,
	[recipient_telegram__id] [int] NULL,
	[telegram_messages_types__id] [int] NULL,
	[created_by] [int] NULL,
	[modified_by] [int] NULL,
	)

/*
CREATE TABLE [ss].[telegram_messages](
	[id] [int] NULL,
	[recipient_telegram__id] [int] NULL,
	[telegram_messages_types__id] [int] NULL,
	[text] [nvarchar](4000) NULL,
	[status_alias] [nvarchar](20) NULL,
	[error_description] [nvarchar](100) NULL,
	[created_at] [datetime] NULL,
	[created_by] [int] NULL,
	[created_ip] [nvarchar](100) NULL,
	[modified_at] [datetime] NULL,
	[modified_by] [int] NULL,
	[modified_ip] [nvarchar](100) NULL,
	[timestamp] [datetime] NULL,
	[sfDate] [datetimeoffset](7) NULL,
	[sfUUID] [uniqueidentifier] NULL
	)
--*/

