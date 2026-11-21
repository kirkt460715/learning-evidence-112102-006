# 记录格式

任务观察以 id、task、version、hint_level、duration_minutes、help_requests、access_issue 表示任务支持、观察时长及可及性记录。时长和求助数不代表认知投入。

记录以 UTF-8 JSON 保存，顶层包含 dataset 和 records。每条记录的 id 在文件中唯一。`fixtures/records.json` 中的例子用于说明输入字段和状态取值。
