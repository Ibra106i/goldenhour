import json

rm = "D:/Ibrahim106/Downloads/goldenhour/README.md"
bp = "D:/Ibrahim106/Downloads/goldenhour/brag-output-2026-09-19-153000/brag-plan.md"
cb = "D:/Ibrahim106/Downloads/goldenhour/brag-output-2026-09-19-153000/composition-brief.md"

def n(id, label, ft, sf):
    return {"id":id,"label":label,"file_type":ft,"source_file":sf,"source_location":None,"source_url":None,"captured_at":None,"author":None,"contributor":None}

def e(src, tgt, rel, conf, sf, cs=None):
    if cs is None:
        cs = 1.0 if conf == "EXTRACTED" else 0.85
    return {"source":src,"target":tgt,"relation":rel,"confidence":conf,"confidence_score":cs,"source_file":sf,"source_location":None,"weight":1.0}

nodes = [
    n("readme","README","document",rm),
    n("readme_gemini_api_key","GEMINI_API_KEY environment variable","concept",rm),
    n("readme_ai_studio","AI Studio platform","concept",rm),
    n("brag_output_2026_09_19_153000_brag_plan","Brag Plan: Golden Hour Coffee Co.","document",bp),
    n("brag_output_2026_09_19_153000_brag_plan_slow_mornings_strong_coffee","Slow mornings strong coffee tagline","concept",bp),
    n("brag_output_2026_09_19_153000_brag_plan_linger","linger hook word","concept",bp),
    n("brag_output_2026_09_19_153000_brag_plan_golden_hour_latte","Golden Hour Latte","concept",bp),
    n("brag_output_2026_09_19_153000_brag_plan_whipped_ricotta_toast","Whipped Ricotta Toast","concept",bp),
    n("brag_output_2026_09_19_153000_brag_plan_cinnamon_roll_skillet","Cinnamon Roll Skillet","concept",bp),
    n("brag_output_2026_09_19_153000_brag_plan_loved_by_locals","Loved by Locals testimonials section","concept",bp),
    n("brag_output_2026_09_19_153000_brag_plan_visual_identity","Visual Identity System","concept",bp),
    n("brag_output_2026_09_19_153000_brag_plan_audio_direction","Audio Direction","concept",bp),
    n("brag_output_2026_09_19_153000_brag_plan_scene_1_the_golden_light","Scene 1 The Golden Light","concept",bp),
    n("brag_output_2026_09_19_153000_brag_plan_scene_2_the_promise","Scene 2 The Promise","concept",bp),
    n("brag_output_2026_09_19_153000_brag_plan_scene_3_from_the_kitchen","Scene 3 From the Kitchen","concept",bp),
    n("brag_output_2026_09_19_153000_brag_plan_scene_4_loved_by_locals","Scene 4 Loved by Locals","concept",bp),
    n("brag_output_2026_09_19_153000_brag_plan_scene_5_the_logo","Scene 5 The Logo","concept",bp),
    n("brag_output_2026_09_19_153000_brag_plan_preset_polished","polished preset tone","rationale",bp),
    n("brag_output_2026_09_19_153000_brag_plan_creative_direction_quiet_premium","quiet premium neighborhood cafe film","rationale",bp),
    n("brag_output_2026_09_19_153000_brag_plan_confidence_through_restraint","Confidence through restraint","rationale",bp),
    n("brag_output_2026_09_19_153000_brag_plan_no_cta_needed","No CTA needed rationale","rationale",bp),
    n("brag_output_2026_09_19_153000_brag_plan_no_restraint_rule","Restraint rule no energetic beats","rationale",bp),
    n("brag_output_2026_09_19_153000_brag_plan_user_flow_note","User flow note landing page only","concept",bp),
    n("brag_output_2026_09_19_153000_brag_plan_share_copy_draft","Share copy draft","document",bp),
    n("brag_output_2026_09_19_153000_composition_brief","Composition Brief Golden Hour Coffee Co.","document",cb),
    n("brag_output_2026_09_19_153000_composition_brief_storyboard_ref","Storyboard reference","document",cb),
    n("brag_output_2026_09_19_153000_composition_brief_source_material","Source Material reference","document",cb),
    n("brag_output_2026_09_19_153000_composition_brief_creative_direction","Creative Direction specification","rationale",cb),
    n("brag_output_2026_09_19_153000_composition_brief_audio_spec","Audio specification","concept",cb),
    n("brag_output_2026_09_19_153000_composition_brief_music_track","happy-beats-business-moves-vol-12 music track","concept",cb),
    n("brag_output_2026_09_19_153000_composition_brief_hyperframes_instructions","Hyperframes Instructions","document",cb),
    n("brag_output_2026_09_19_153000_composition_brief_hyperframes_core","Hyperframes Core skill","concept",cb),
    n("brag_output_2026_09_19_153000_composition_brief_hyperframes_animation","Hyperframes Animation skill","concept",cb),
    n("brag_output_2026_09_19_153000_composition_brief_hyperframes_creative","Hyperframes Creative skill","concept",cb),
    n("brag_output_2026_09_19_153000_composition_brief_hyperframes_keyframes","Hyperframes Keyframes skill","concept",cb),
    n("brag_output_2026_09_19_153000_composition_brief_hyperframes_cli","Hyperframes CLI skill","concept",cb),
]

edges = [
    e("brag_output_2026_09_19_153000_brag_plan","readme","references","EXTRACTED",bp),
    e("brag_output_2026_09_19_153000_brag_plan","brag_output_2026_09_19_153000_brag_plan_slow_mornings_strong_coffee","references","EXTRACTED",bp),
    e("brag_output_2026_09_19_153000_brag_plan","brag_output_2026_09_19_153000_brag_plan_linger","references","EXTRACTED",bp),
    e("brag_output_2026_09_19_153000_brag_plan","brag_output_2026_09_19_153000_brag_plan_scene_1_the_golden_light","references","EXTRACTED",bp),
    e("brag_output_2026_09_19_153000_brag_plan","brag_output_2026_09_19_153000_brag_plan_scene_2_the_promise","references","EXTRACTED",bp),
    e("brag_output_2026_09_19_153000_brag_plan","brag_output_2026_09_19_153000_brag_plan_scene_3_from_the_kitchen","references","EXTRACTED",bp),
    e("brag_output_2026_09_19_153000_brag_plan","brag_output_2026_09_19_153000_brag_plan_scene_4_loved_by_locals","references","EXTRACTED",bp),
    e("brag_output_2026_09_19_153000_brag_plan","brag_output_2026_09_19_153000_brag_plan_scene_5_the_logo","references","EXTRACTED",bp),
    e("brag_output_2026_09_19_153000_brag_plan","brag_output_2026_09_19_153000_brag_plan_visual_identity","references","EXTRACTED",bp),
    e("brag_output_2026_09_19_153000_brag_plan","brag_output_2026_09_19_153000_brag_plan_audio_direction","references","EXTRACTED",bp),
    e("brag_output_2026_09_19_153000_brag_plan","brag_output_2026_09_19_153000_brag_plan_golden_hour_latte","references","EXTRACTED",bp),
    e("brag_output_2026_09_19_153000_brag_plan","brag_output_2026_09_19_153000_brag_plan_whipped_ricotta_toast","references","EXTRACTED",bp),
    e("brag_output_2026_09_19_153000_brag_plan","brag_output_2026_09_19_153000_brag_plan_cinnamon_roll_skillet","references","EXTRACTED",bp),
    e("brag_output_2026_09_19_153000_brag_plan","brag_output_2026_09_19_153000_brag_plan_loved_by_locals","references","EXTRACTED",bp),
    e("brag_output_2026_09_19_153000_brag_plan","brag_output_2026_09_19_153000_brag_plan_preset_polished","references","EXTRACTED",bp),
    e("brag_output_2026_09_19_153000_brag_plan","brag_output_2026_09_19_153000_brag_plan_creative_direction_quiet_premium","references","EXTRACTED",bp),
    e("brag_output_2026_09_19_153000_brag_plan","brag_output_2026_09_19_153000_brag_plan_confidence_through_restraint","references","EXTRACTED",bp),
    e("brag_output_2026_09_19_153000_brag_plan","brag_output_2026_09_19_153000_brag_plan_user_flow_note","references","EXTRACTED",bp),
    e("brag_output_2026_09_19_153000_brag_plan","brag_output_2026_09_19_153000_brag_plan_share_copy_draft","references","EXTRACTED",bp),
    e("brag_output_2026_09_19_153000_brag_plan","brag_output_2026_09_19_153000_brag_plan_no_cta_needed","references","EXTRACTED",bp),
    e("brag_output_2026_09_19_153000_brag_plan","brag_output_2026_09_19_153000_brag_plan_no_restraint_rule","references","EXTRACTED",bp),
    e("brag_output_2026_09_19_153000_composition_brief","brag_output_2026_09_19_153000_brag_plan","references","EXTRACTED",cb),
    e("brag_output_2026_09_19_153000_composition_brief","brag_output_2026_09_19_153000_composition_brief_storyboard_ref","references","EXTRACTED",cb),
    e("brag_output_2026_09_19_153000_composition_brief","brag_output_2026_09_19_153000_composition_brief_source_material","references","EXTRACTED",cb),
    e("brag_output_2026_09_19_153000_composition_brief","brag_output_2026_09_19_153000_composition_brief_creative_direction","references","EXTRACTED",cb),
    e("brag_output_2026_09_19_153000_composition_brief","brag_output_2026_09_19_153000_composition_brief_audio_spec","references","EXTRACTED",cb),
    e("brag_output_2026_09_19_153000_composition_brief","brag_output_2026_09_19_153000_composition_brief_music_track","references","EXTRACTED",cb),
    e("brag_output_2026_09_19_153000_composition_brief","brag_output_2026_09_19_153000_composition_brief_hyperframes_instructions","references","EXTRACTED",cb),
    e("brag_output_2026_09_19_153000_composition_brief","brag_output_2026_09_19_153000_composition_brief_hyperframes_core","references","EXTRACTED",cb),
    e("brag_output_2026_09_19_153000_composition_brief","brag_output_2026_09_19_153000_composition_brief_hyperframes_animation","references","EXTRACTED",cb),
    e("brag_output_2026_09_19_153000_composition_brief","brag_output_2026_09_19_153000_composition_brief_hyperframes_creative","references","EXTRACTED",cb),
    e("brag_output_2026_09_19_153000_composition_brief","brag_output_2026_09_19_153000_composition_brief_hyperframes_keyframes","references","EXTRACTED",cb),
    e("brag_output_2026_09_19_153000_composition_brief","brag_output_2026_09_19_153000_composition_brief_hyperframes_cli","references","EXTRACTED",cb),
    e("brag_output_2026_09_19_153000_composition_brief_storyboard_ref","brag_output_2026_09_19_153000_brag_plan_scene_1_the_golden_light","references","EXTRACTED",cb),
    e("brag_output_2026_09_19_153000_composition_brief_storyboard_ref","brag_output_2026_09_19_153000_brag_plan_scene_2_the_promise","references","EXTRACTED",cb),
    e("brag_output_2026_09_19_153000_composition_brief_storyboard_ref","brag_output_2026_09_19_153000_brag_plan_scene_3_from_the_kitchen","references","EXTRACTED",cb),
    e("brag_output_2026_09_19_153000_composition_brief_storyboard_ref","brag_output_2026_09_19_153000_brag_plan_scene_4_loved_by_locals","references","EXTRACTED",cb),
    e("brag_output_2026_09_19_153000_composition_brief_storyboard_ref","brag_output_2026_09_19_153000_brag_plan_scene_5_the_logo","references","EXTRACTED",cb),
    e("brag_output_2026_09_19_153000_composition_brief_source_material","readme","references","EXTRACTED",cb),
    e("brag_output_2026_09_19_153000_composition_brief_hyperframes_instructions","brag_output_2026_09_19_153000_composition_brief_hyperframes_core","references","EXTRACTED",cb),
    e("brag_output_2026_09_19_153000_composition_brief_hyperframes_instructions","brag_output_2026_09_19_153000_composition_brief_hyperframes_animation","references","EXTRACTED",cb),
    e("brag_output_2026_09_19_153000_composition_brief_hyperframes_instructions","brag_output_2026_09_19_153000_composition_brief_hyperframes_creative","references","EXTRACTED",cb),
    e("brag_output_2026_09_19_153000_composition_brief_hyperframes_instructions","brag_output_2026_09_19_153000_composition_brief_hyperframes_keyframes","references","EXTRACTED",cb),
    e("brag_output_2026_09_19_153000_composition_brief_hyperframes_instructions","brag_output_2026_09_19_153000_composition_brief_hyperframes_cli","references","EXTRACTED",cb),
    e("brag_output_2026_09_19_153000_composition_brief_audio_spec","brag_output_2026_09_19_153000_brag_plan_audio_direction","conceptually_related_to","EXTRACTED",cb),
    e("brag_output_2026_09_19_153000_composition_brief_creative_direction","brag_output_2026_09_19_153000_brag_plan_creative_direction_quiet_premium","conceptually_related_to","EXTRACTED",cb),
    e("brag_output_2026_09_19_153000_brag_plan_scene_1_the_golden_light","brag_output_2026_09_19_153000_brag_plan_linger","references","EXTRACTED",bp),
    e("brag_output_2026_09_19_153000_brag_plan_scene_2_the_promise","brag_output_2026_09_19_153000_brag_plan_slow_mornings_strong_coffee","references","EXTRACTED",bp),
    e("brag_output_2026_09_19_153000_brag_plan_scene_3_from_the_kitchen","brag_output_2026_09_19_153000_brag_plan_golden_hour_latte","references","EXTRACTED",bp),
    e("brag_output_2026_09_19_153000_brag_plan_scene_3_from_the_kitchen","brag_output_2026_09_19_153000_brag_plan_whipped_ricotta_toast","references","EXTRACTED",bp),
    e("brag_output_2026_09_19_153000_brag_plan_scene_3_from_the_kitchen","brag_output_2026_09_19_153000_brag_plan_cinnamon_roll_skillet","references","EXTRACTED",bp),
    e("brag_output_2026_09_19_153000_brag_plan_scene_4_loved_by_locals","brag_output_2026_09_19_153000_brag_plan_loved_by_locals","references","EXTRACTED",bp),
    e("brag_output_2026_09_19_153000_brag_plan_creative_direction_quiet_premium","brag_output_2026_09_19_153000_brag_plan_confidence_through_restraint","conceptually_related_to","INFERRED",bp,0.85),
    e("brag_output_2026_09_19_153000_brag_plan_confidence_through_restraint","brag_output_2026_09_19_153000_brag_plan_no_cta_needed","rationale_for","INFERRED",bp,0.85),
    e("brag_output_2026_09_19_153000_brag_plan_no_restraint_rule","brag_output_2026_09_19_153000_brag_plan_creative_direction_quiet_premium","rationale_for","INFERRED",bp,0.85),
    e("brag_output_2026_09_19_153000_brag_plan_linger","brag_output_2026_09_19_153000_brag_plan_slow_mornings_strong_coffee","semantically_similar_to","INFERRED",bp,0.75),
]

hyperedges = [
    {
        "id": "storyboard_five_scenes",
        "label": "Five-scene storyboard arc",
        "nodes": [
            "brag_output_2026_09_19_153000_brag_plan_scene_1_the_golden_light",
            "brag_output_2026_09_19_153000_brag_plan_scene_2_the_promise",
            "brag_output_2026_09_19_153000_brag_plan_scene_3_from_the_kitchen",
            "brag_output_2026_09_19_153000_brag_plan_scene_4_loved_by_locals",
            "brag_output_2026_09_19_153000_brag_plan_scene_5_the_logo",
        ],
        "relation": "participate_in",
        "confidence": "EXTRACTED",
        "confidence_score": 1.0,
        "source_file": bp,
    },
    {
        "id": "hyperframes_skill_stack",
        "label": "Hyperframes skill stack for composition",
        "nodes": [
            "brag_output_2026_09_19_153000_composition_brief_hyperframes_core",
            "brag_output_2026_09_19_153000_composition_brief_hyperframes_animation",
            "brag_output_2026_09_19_153000_composition_brief_hyperframes_creative",
            "brag_output_2026_09_19_153000_composition_brief_hyperframes_keyframes",
            "brag_output_2026_09_19_153000_composition_brief_hyperframes_cli",
        ],
        "relation": "implement",
        "confidence": "EXTRACTED",
        "confidence_score": 1.0,
        "source_file": cb,
    },
    {
        "id": "three_featured_dishes",
        "label": "Three featured dishes in Scene 3",
        "nodes": [
            "brag_output_2026_09_19_153000_brag_plan_golden_hour_latte",
            "brag_output_2026_09_19_153000_brag_plan_whipped_ricotta_toast",
            "brag_output_2026_09_19_153000_brag_plan_cinnamon_roll_skillet",
        ],
        "relation": "participate_in",
        "confidence": "EXTRACTED",
        "confidence_score": 1.0,
        "source_file": bp,
    },
]

result = {
    "nodes": nodes,
    "edges": edges,
    "hyperedges": hyperedges,
    "input_tokens": 0,
    "output_tokens": 0,
}

out = "D:/Ibrahim106/Downloads/goldenhour/graphify-out/.graphify_chunk_01.json"
with open(out, "w", encoding="utf-8") as f:
    json.dump(result, f, indent=2)
print(f"Written {len(nodes)} nodes, {len(edges)} edges, {len(hyperedges)} hyperedges to {out}")
