from singer_sdk import typing as th

usersSchema = th.PropertiesList(
    th.Property("id",th.StringType),
    th.Property("nama",th.StringType),
    th.Property("active",th.BooleanType),
    th.Property("admin",th.BooleanType),
    th.Property("createdAt",th.DateTimeType),
    th.Property("archivedAt",th.DateTimeType),
    th.Property("description",th.StringType),
    th.Property("avatarUrl",th.StringType),
    th.Property("displayName",th.StringType),
    th.Property("email",th.StringType),
    th.Property("guest",th.BooleanType),
    th.Property("lastSeen",th.DateTimeType),
    th.Property("organization",
        th.ObjectType(
            th.Property("id",th.StringType),
            th.Property("name",th.StringType),
        )
    ),
    th.Property("statusLabel",th.StringType),
    th.Property("statusUnitAt",th.DateTimeType),
    th.Property("timezone",th.StringType),
    th.Property("updatedAt",th.DateTimeType),
    th.Property("url",th.StringType),
    th.Property("calendarHash",th.StringType),
    th.Property("inviteHash",th.StringType),
    th.Property("createdIssueCount",th.IntegerType),
    th.Property("disableReason",th.StringType),
    th.Property("isMe",th.BooleanType),
    th.Property("statusEmoji",th.StringType),
    th.Property("statusUntilAt",th.DateTimeType),
).to_dict()
