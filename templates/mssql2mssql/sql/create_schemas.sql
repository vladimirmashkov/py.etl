if NOT EXISTS (select [name] from [sys].[schemas] where [name] = 'ss') exec sp_executesql N'create schema [ss]';
if NOT EXISTS (select [name] from [sys].[schemas] where [name] = 'store') exec sp_executesql N'create schema [store]';
if NOT EXISTS (select [name] from [sys].[schemas] where [name] = 'temp') exec sp_executesql N'create schema [temp]';
if NOT EXISTS (select [name] from [sys].[schemas] where [name] = 'sd') exec sp_executesql N'create schema [sd]';
if NOT EXISTS (select [name] from [sys].[schemas] where [name] = 'temp_store') exec sp_executesql N'create schema [temp_store]';
if NOT EXISTS (select [name] from [sys].[schemas] where [name] = 'temp_sd') exec sp_executesql N'create schema [temp_sd]';

