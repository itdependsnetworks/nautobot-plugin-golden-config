# Generated by Django 3.1.8 on 2021-05-04 05:19

import django.core.serializers.json
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re
import taggit.managers
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("dcim", "0004_initial_part_4"),
        ("extras", "0004_populate_default_status_records"),
    ]

    operations = [
        migrations.CreateModel(
            name="ComplianceFeature",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("created", models.DateField(auto_now_add=True, null=True)),
                ("last_updated", models.DateTimeField(auto_now=True, null=True)),
                (
                    "_custom_field_data",
                    models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=255,
                        validators=[
                            django.core.validators.RegexValidator(
                                re.compile("^[-a-zA-Z0-9_]+\\Z"),
                                "Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.",
                                "invalid",
                            )
                        ],
                    ),
                ),
                ("tags", taggit.managers.TaggableManager(through="extras.TaggedItem", to="extras.Tag")),
            ],
            options={
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="ComplianceRule",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("created", models.DateField(auto_now_add=True, null=True)),
                ("last_updated", models.DateTimeField(auto_now=True, null=True)),
                (
                    "_custom_field_data",
                    models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder),
                ),
                ("description", models.CharField(blank=True, max_length=200)),
                ("config_ordered", models.BooleanField()),
                ("match_config", models.TextField(null=True)),
                ("config_type", models.CharField(default="cli", max_length=20)),
                (
                    "feature",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="feature",
                        to="nautobot_golden_config.compliancefeature",
                    ),
                ),
                (
                    "platform",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="compliance_rules", to="dcim.platform"
                    ),
                ),
                ("tags", taggit.managers.TaggableManager(through="extras.TaggedItem", to="extras.Tag")),
            ],
            options={
                "ordering": ("platform", "feature__name"),
                "unique_together": {("feature", "platform")},
            },
        ),
        migrations.CreateModel(
            name="GoldenConfiguration",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("created", models.DateField(auto_now_add=True, null=True)),
                ("last_updated", models.DateTimeField(auto_now=True, null=True)),
                (
                    "_custom_field_data",
                    models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder),
                ),
                ("backup_config", models.TextField(blank=True)),
                ("backup_last_attempt_date", models.DateTimeField(null=True)),
                ("backup_last_success_date", models.DateTimeField(null=True)),
                ("intended_config", models.TextField(blank=True)),
                ("intended_last_attempt_date", models.DateTimeField(null=True)),
                ("intended_last_success_date", models.DateTimeField(null=True)),
                ("compliance_config", models.TextField(blank=True)),
                ("compliance_last_attempt_date", models.DateTimeField(null=True)),
                ("compliance_last_success_date", models.DateTimeField(null=True)),
                ("device", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="dcim.device")),
                ("tags", taggit.managers.TaggableManager(through="extras.TaggedItem", to="extras.Tag")),
            ],
            options={
                "ordering": ["device"],
            },
        ),
        migrations.CreateModel(
            name="GoldenConfigSettings",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("created", models.DateField(auto_now_add=True, null=True)),
                ("last_updated", models.DateTimeField(auto_now=True, null=True)),
                (
                    "_custom_field_data",
                    models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder),
                ),
                ("backup_path_template", models.CharField(blank=True, max_length=255)),
                ("intended_path_template", models.CharField(blank=True, max_length=255)),
                ("jinja_path_template", models.CharField(blank=True, max_length=255)),
                ("backup_test_connectivity", models.BooleanField(default=True)),
                ("shorten_sot_query", models.BooleanField(default=False)),
                ("sot_agg_query", models.TextField(blank=True)),
                ("only_primary_ip", models.BooleanField(default=False)),
                ("exclude_chassis_members", models.BooleanField(default=False)),
                ("tags", taggit.managers.TaggableManager(through="extras.TaggedItem", to="extras.Tag")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ConfigReplace",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("created", models.DateField(auto_now_add=True, null=True)),
                ("last_updated", models.DateTimeField(auto_now=True, null=True)),
                (
                    "_custom_field_data",
                    models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder),
                ),
                ("name", models.CharField(max_length=255)),
                ("description", models.CharField(blank=True, max_length=200)),
                ("substitute_text", models.CharField(max_length=200)),
                ("replaced_text", models.CharField(max_length=200)),
                (
                    "platform",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="backup_line_replace",
                        to="dcim.platform",
                    ),
                ),
                ("tags", taggit.managers.TaggableManager(through="extras.TaggedItem", to="extras.Tag")),
            ],
            options={
                "ordering": ("platform", "name"),
                "unique_together": {("name", "platform")},
            },
        ),
        migrations.CreateModel(
            name="ConfigRemove",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("created", models.DateField(auto_now_add=True, null=True)),
                ("last_updated", models.DateTimeField(auto_now=True, null=True)),
                (
                    "_custom_field_data",
                    models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder),
                ),
                ("name", models.CharField(max_length=255)),
                ("description", models.CharField(blank=True, max_length=200)),
                ("regex_line", models.CharField(max_length=200)),
                (
                    "platform",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="backup_line_remove",
                        to="dcim.platform",
                    ),
                ),
                ("tags", taggit.managers.TaggableManager(through="extras.TaggedItem", to="extras.Tag")),
            ],
            options={
                "ordering": ("platform", "name"),
                "unique_together": {("name", "platform")},
            },
        ),
        migrations.CreateModel(
            name="ConfigCompliance",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("created", models.DateField(auto_now_add=True, null=True)),
                ("last_updated", models.DateTimeField(auto_now=True, null=True)),
                (
                    "_custom_field_data",
                    models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder),
                ),
                ("compliance", models.BooleanField(blank=True, null=True)),
                ("actual", models.TextField(blank=True)),
                ("intended", models.TextField(blank=True)),
                ("missing", models.TextField(blank=True)),
                ("extra", models.TextField(blank=True)),
                ("ordered", models.BooleanField(default=True)),
                ("device", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="dcim.device")),
                (
                    "rule",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="rule",
                        to="nautobot_golden_config.compliancerule",
                    ),
                ),
                ("tags", taggit.managers.TaggableManager(through="extras.TaggedItem", to="extras.Tag")),
            ],
            options={
                "ordering": ["device"],
                "unique_together": {("device", "rule")},
            },
        ),
    ]
