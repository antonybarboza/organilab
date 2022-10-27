# Generated by Django 4.0.8 on 2022-10-20 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sga', '0037_merge_20221020_0030'),
    ]

    operations = [
        migrations.RunSQL("""
BEGIN;
SELECT setval(pg_get_serial_sequence('"sga_warningclass"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "sga_warningclass";
SELECT setval(pg_get_serial_sequence('"sga_warningword"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "sga_warningword";
SELECT setval(pg_get_serial_sequence('"sga_prudenceadvice"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "sga_prudenceadvice";
SELECT setval(pg_get_serial_sequence('"sga_dangerindication_pictograms"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "sga_dangerindication_pictograms";
SELECT setval(pg_get_serial_sequence('"sga_dangerindication_warning_class"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "sga_dangerindication_warning_class";
SELECT setval(pg_get_serial_sequence('"sga_dangerindication_warning_category"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "sga_dangerindication_warning_category";
SELECT setval(pg_get_serial_sequence('"sga_dangerindication_prudence_advice"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "sga_dangerindication_prudence_advice";
SELECT setval(pg_get_serial_sequence('"sga_dangerprudence_danger_indication"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "sga_dangerprudence_danger_indication";
SELECT setval(pg_get_serial_sequence('"sga_dangerprudence_prudence_advice"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "sga_dangerprudence_prudence_advice";
SELECT setval(pg_get_serial_sequence('"sga_dangerprudence"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "sga_dangerprudence";
SELECT setval(pg_get_serial_sequence('"sga_component"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "sga_component";
SELECT setval(pg_get_serial_sequence('"sga_substance_components_sga"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "sga_substance_components_sga";
SELECT setval(pg_get_serial_sequence('"sga_substance_danger_indications"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "sga_substance_danger_indications";
SELECT setval(pg_get_serial_sequence('"sga_substance"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "sga_substance";
SELECT setval(pg_get_serial_sequence('"sga_substancecharacteristics_white_organ"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "sga_substancecharacteristics_white_organ";
SELECT setval(pg_get_serial_sequence('"sga_substancecharacteristics_h_code"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "sga_substancecharacteristics_h_code";
SELECT setval(pg_get_serial_sequence('"sga_substancecharacteristics_ue_code"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "sga_substancecharacteristics_ue_code";
SELECT setval(pg_get_serial_sequence('"sga_substancecharacteristics_nfpa"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "sga_substancecharacteristics_nfpa";
SELECT setval(pg_get_serial_sequence('"sga_substancecharacteristics_storage_class"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "sga_substancecharacteristics_storage_class";
SELECT setval(pg_get_serial_sequence('"sga_substancecharacteristics"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "sga_substancecharacteristics";
SELECT setval(pg_get_serial_sequence('"sga_builderinformation"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "sga_builderinformation";
SELECT setval(pg_get_serial_sequence('"sga_recipientsize"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "sga_recipientsize";
SELECT setval(pg_get_serial_sequence('"sga_label"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "sga_label";
SELECT setval(pg_get_serial_sequence('"sga_templatesga"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "sga_templatesga";
SELECT setval(pg_get_serial_sequence('"sga_personaltemplatesga"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "sga_personaltemplatesga";
SELECT setval(pg_get_serial_sequence('"sga_donation"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "sga_donation";
SELECT setval(pg_get_serial_sequence('"sga_sgacomplement_danger_indication"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "sga_sgacomplement_danger_indication";
SELECT setval(pg_get_serial_sequence('"sga_sgacomplement_prudence_advice"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "sga_sgacomplement_prudence_advice";
SELECT setval(pg_get_serial_sequence('"sga_sgacomplement_pictograms"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "sga_sgacomplement_pictograms";
SELECT setval(pg_get_serial_sequence('"sga_sgacomplement"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "sga_sgacomplement";
SELECT setval(pg_get_serial_sequence('"sga_provider"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "sga_provider";
SELECT setval(pg_get_serial_sequence('"sga_securityleaf"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "sga_securityleaf";
SELECT setval(pg_get_serial_sequence('"sga_reviewsubstance"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "sga_reviewsubstance";
COMMIT; """)
    ]
