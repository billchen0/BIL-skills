export const slideFormats = [
  { id:'title', name:'Title', purpose:'Orient the room with the meeting topic and framing.', hooks:['slide-stage','slide-title','title-block','top-badge'] },
  { id:'section', name:'Section divider', purpose:'Create a calm transition between narrative chapters.', hooks:['slide-stage','slide-section','section-divider'] },
  { id:'research', name:'Research update', purpose:'Pair a focused update with an abstract figure placeholder.', hooks:['slide-stage','slide-research','content-grid','figure-placeholder'] },
  { id:'methods', name:'Methods / workflow', purpose:'Show a readable sequence of actions or protocol stages.', hooks:['slide-stage','slide-methods','workflow','step-badge'] },
  { id:'results', name:'Results + takeaway', purpose:'Place a non-data-bearing figure beside one explicit interpretation.', hooks:['slide-stage','slide-results','results-grid','callout'] },
  { id:'comparison', name:'Comparison', purpose:'Compare two approaches with parallel anatomy.', hooks:['slide-stage','slide-comparison','comparison'] },
  { id:'timeline', name:'Timeline / next steps', purpose:'Show sequence, dependencies, and the active next step.', hooks:['slide-stage','rail','node','timeline-label'] },
  { id:'discussion', name:'Discussion / decision', purpose:'Frame options and the decision needed from the room.', hooks:['slide-stage','slide-discussion','decision-grid'] },
  { id:'closing', name:'Closing', purpose:'End with a concise prompt or discussion invitation.', hooks:['slide-stage','slide-closing','title-block'] },
  { id:'profile', name:'Profile timeline', purpose:'Reference-derived profile and trajectory format.', hooks:['slide-stage','slide-profile','profile-card','trajectory'] }
];
