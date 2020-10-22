$work_dir=Split-Path -parent $MyInvocation.MyCommand.Definition
protoc --proto_path=$work_dir --python_out=$work_dir $work_dir"\*.proto"