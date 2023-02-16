# Copyright The IETF Trust 2022, All Rights Reserved# Generated by Django 2.2.28 on 2022-12-22 22:41

from django.db import migrations


def forward(apps, schema_editor):
    Recipient = apps.get_model("mailtrigger", "Recipient")
    MailTrigger = apps.get_model("mailtrigger", "MailTrigger")

    rsab = Recipient.objects.create(
        slug="rsab",
        desc="The RFC Series Approval Board",
        template="The RSAB <rsab@rfc-editor.org>",
    )

    rsab_ballot_saved = MailTrigger.objects.create(
        slug="rsab_ballot_saved",
        desc="Recipients when a new RSAB ballot position with comments is saved",
    )
    rsab_ballot_saved.to.add(rsab)
    rsab_ballot_saved.cc.set(
        Recipient.objects.filter(
            slug__in=[
                "doc_affecteddoc_authors",
                "doc_affecteddoc_group_chairs",
                "doc_affecteddoc_notify",
                "doc_authors",
                "doc_group_chairs",
                "doc_group_mail_list",
                "doc_notify",
                "doc_shepherd",
            ]
        )
    )

    rsab_ballot_issued = MailTrigger.objects.create(
        slug="rsab_ballot_issued",
        desc="Recipients when a new RSAB ballot is issued",
    )
    rsab_ballot_issued.to.add(rsab)
    rsab_ballot_issued.cc.set(
        Recipient.objects.filter(
            slug__in=[
                "doc_affecteddoc_authors",
                "doc_affecteddoc_group_chairs",
                "doc_affecteddoc_notify",
                "doc_authors",
                "doc_group_chairs",
                "doc_group_mail_list",
                "doc_notify",
                "doc_shepherd",
            ]
        )
    )


def reverse(apps, schema_editor):
    Recipient = apps.get_model("mailtrigger", "Recipient")
    MailTrigger = apps.get_model("mailtrigger", "MailTrigger")
    MailTrigger.objects.filter(
        slug__in=("rsab_ballot_issued", "rsab_ballot_saved")
    ).delete()
    Recipient.objects.filter(slug="rsab").delete()


class Migration(migrations.Migration):

    dependencies = [
        ("mailtrigger", "0023_bofreq_triggers"),
    ]

    operations = [migrations.RunPython(forward, reverse)]